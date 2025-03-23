styles = """<style>    
    .stAppHeader, .footer {
        display: none !important
    }

    <div></div>
    
    .stApp {
        background-color: aqua;
        position: relative;
    }


    .stMain {
        position: absolute;
        inset: 0;
        z-index: 10;
        height: 100vh;
        width: 100vw;
        align-items: center;
        padding: 6rem1.25rem;
        overflow: hidden;
        background: radial-gradient(125% 125% at 50% 10%, #000 40%, #63e 100%)

    }   
    
    .stMainm {
        position: absolute;
        top: 0;
        z-index: 2;
        height: 100vh;
        width: 100vw;
        background-color: white;
        background: radial-gradient(
            100% 50% at 50% 0%, 
            rgba(0, 163, 255, 0.13) 0, 
            rgba(0, 163, 255, 0) 50%, 
            rgba(0, 163, 255, 0) 100%
        )
    }
    
    .st-emotion-cache-0 {
        background-color: #eee;
        border-radius: 1rem;
    }

    #heading {
        text-align: center;
    }

    #question {
        font-size: 1.5rem;
    }

    .stMarkdown p {
        margin: 0;
    }

    .questions {
        position: absolute;
        right: 2rem;
        top: 6rem;
        font-weight: 600;
    }

    .st-key-container {
        padding: 1rem 2rem;
        gap: 0.5rem;
    }
    
    .st-key-footer {
        position: fixed; 
        bottom: 1.2rem;
        text-align: center;
        color: #fff
    }
</style>"""
