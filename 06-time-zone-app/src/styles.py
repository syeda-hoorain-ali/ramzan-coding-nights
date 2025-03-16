from pandas import DataFrame


styles = """<style>    
    .stAppHeader, .footer {
        display: none !important
    }
    
    .st-emotion-cache-0 {
        background-color: white;
        text-align: center;
        border-radius: 1rem;
    }

    .st-key-container {
        padding: 1rem 2rem;
        gap: 0.5rem;
    }

    .stAlertContainer {
        color: green;
    }

    .dvn-underlay * {
        background-color: red;
        color: red !important;
    }


    div[data-baseweb="popover"] ul {
        background-color: ghostwhite !important;
    }
    
    .st-key-footer {
        position: fixed; 
        bottom: 0px;
        background: aqua;
    }
</style>"""


def style_dataframe(df: DataFrame):
    return df.style.set_table_styles(
        [{
            'selector': 'th',
            'props': [
                ('background-color', 'blue'),
                ('color', 'white'),
                ('font-family', 'Arial, sans-serif'),
                ('font-weight', 'bold'),
                ('border', '2px solid blue')
            ]
        }, 
        {
            'selector': 'td',
            'props': [
                ('width', '50%'),
            ]
        }]
    )