import pandas as pd
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

data_path = "twitter_dataset.csv"  
df = pd.read_csv(data_path)

df["created_at"] = pd.to_datetime(df["created_at"], format="%d-%m-%Y %H:%M", errors="coerce")
df["hour"] = df["created_at"].dt.hour

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
app.title = "TREND FORECASTER"

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("TREND FORECASTER", className="text-center text-light mb-2"), width=12),
        dbc.Col(html.P("Enter a keyword in the search bar to explore real-time social media trends.",
                       className="text-center text-muted"), width=12)
    ]),

    dbc.Row(
        dbc.Col(
            dbc.Input(id="trend-search", placeholder="Search for trends or hashtags...", type="text"),
            width=6, className="offset-md-3 mb-4" 
        ),
    ),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Most Used Word", className="card-title"),
                html.H2(id="most-used-word", className="card-text"),
                html.I(className="bi bi-chat-text", style={"fontSize": "2rem"})
            ])
        ], className="mb-3 shadow-sm", style={"backgroundColor": "#333", "color": "white", "border": "1px solid #555"}), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Hourly Activity", className="card-title"),
                html.H2(id="hourly-activity", className="card-text"),
                html.I(className="bi bi-clock-history", style={"fontSize": "2rem"})
            ])
        ], className="mb-3 shadow-sm", style={"backgroundColor": "#333", "color": "white", "border": "1px solid #555"}), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Tweets Count", className="card-title"),
                html.H2(len(df), className="card-text"),
                html.I(className="bi bi-hash", style={"fontSize": "2rem"})
            ])
        ], className="mb-3 shadow-sm", style={"backgroundColor": "#333", "color": "white", "border": "1px solid #555"}), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H5("Total Users", className="card-title"),
                html.H2(df["username"].nunique(), className="card-text"),
                html.I(className="bi bi-people", style={"fontSize": "2rem"})
            ])
        ], className="mb-3 shadow-sm", style={"backgroundColor": "#333", "color": "white", "border": "1px solid #555"}), width=3)
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(id="trending-words-chart"), xs=12, md=6),
        dbc.Col(dcc.Graph(id="hourly-trend-chart"), xs=12, md=6)
    ]),

    dcc.Interval(id="interval-component", interval=60 * 1000, n_intervals=0)
], fluid=True, style={"padding": "20px", "backgroundColor": "#222"})

@app.callback(
    [Output("most-used-word", "children"),
     Output("hourly-activity", "children"),
     Output("trending-words-chart", "figure"),
     Output("hourly-trend-chart", "figure")],
    [Input("interval-component", "n_intervals")],
    [Input("trend-search", "value")]
)
def update_trends(n_intervals, search_query):
    if search_query:
        filtered_df = df[df["tweet"].str.contains(search_query, case=False, na=False)]
        if filtered_df.empty:
            return "No Results", 0, go.Figure(), go.Figure()
        trending_words = filtered_df["tweet"].str.split(expand=True).stack().value_counts().head(10)
        hourly_trends = filtered_df.groupby("hour").size()
    else:
        trending_words = df["tweet"].str.split(expand=True).stack().value_counts().head(10)
        hourly_trends = df.groupby("hour").size()

    most_used_word = trending_words.index[0]
    hourly_activity = hourly_trends.sum()

    trending_title = f"Top Trending Words {'for ' + search_query if search_query else ''}"
    hourly_title = f"Hourly Activity {'for ' + search_query if search_query else ''}"

    trending_fig = go.Figure(data=[
        go.Bar(x=trending_words.index, y=trending_words.values,
               marker=dict(color="#1f77b4"))
    ])
    trending_fig.update_layout(
        title=trending_title,
        xaxis_title="Words", yaxis_title="Frequency",
        plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"),
        margin=dict(l=40, r=40, t=50, b=30)
    )

    hourly_fig = go.Figure(data=[
        go.Scatter(x=hourly_trends.index, y=hourly_trends.values,
                   mode='lines+markers', marker=dict(color="#ff7f0e"))
    ])
    hourly_fig.update_layout(
        title=hourly_title,
        xaxis_title="Hour", yaxis_title="Tweet Count",
        plot_bgcolor="#222", paper_bgcolor="#222", font=dict(color="white"),
        margin=dict(l=40, r=40, t=50, b=30)
    )

    return most_used_word, hourly_activity, trending_fig, hourly_fig

if __name__ == '__main__':
    app.run_server(debug=True)
