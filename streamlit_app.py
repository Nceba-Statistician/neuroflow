import streamlit

streamlit.markdown(
    """
    <style>
        .title {
            position: absolute;
            top: 20;
            right: 0;
            font-size: 20px;
            font-weight: bold;
        }
        </style>
""",
    unsafe_allow_html=True,
)

streamlit.markdown(
    """<div class="title"></div>""", unsafe_allow_html=True
)

neuroflow = streamlit.Page(
    "model-flow/neuroflow.py", title="Neuroflow", icon=":material/settings:", default=False
)
dataready = streamlit.Page(
    "model-flow/upload-data.py", title="Upload data", icon=":material/upload:", default=False
)
preprocessing = streamlit.Page(
    "model-flow/preprocessing.py", title="Preprocessing", icon=":material/settings:", default=False
)

dashboard = streamlit.Page(
    "reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=False
)
history = streamlit.Page(
    "tools/history.py", title="History", icon=":material/history:", default=False
)
search = streamlit.Page(
    "tools/search.py", title="Search", icon=":material/search:", default=False
)

Pages = streamlit.navigation({
    "Model Constructor": [neuroflow, dataready, preprocessing],
    "Reports": [dashboard],
    "Tools": [history, search]
})
Pages.run()