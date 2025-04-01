styles = """<style>    
    .stAppHeader, .footer {
        display: none !important
    }

    .stAppViewContainer {
        height: 100vh;
        background-color: white;
        position: relative;
    } 
    
    section.stMain {
       position: absolute;
        inset: 0;
        z-index: 10;
        height: 100vh;
        width: 100vw;
        align-items: center;
        overflow: hidden;
        background: radial-gradient(70% 70% at center, #fff 30%, rgb(255, 0, 179) 100%)
    } 
    
    .st-emotion-cache-0 {
        background-color: white;
        text-align: center;
        border-radius: 1rem;
        color: black;
    }

    .st-key-container {
        padding: 1rem 2rem;
        gap: 0.5rem;
    }

    .stAlert p {
        color: green;
    }
    
    .st-key-footer {
        position: fixed; 
        bottom: 0px;
        background: linear-gradient(125% 125% at 50% 10%, #fff 30%, rgb(255, 0, 179) 100%)
    }
</style>"""

