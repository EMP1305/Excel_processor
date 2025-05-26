import streamlit

main_page = streamlit.Page('interface.py',title='Main Page',icon='📊')
page2 = streamlit.Page('df_show.py',title='Data Frame',icon='📰')
page3 = streamlit.Page('df_page.py',title='Data Frame properties',icon='💻')
page4 = streamlit.Page('stats_page.py',title='Statistic data',icon='💾')
page5 = streamlit.Page('pred_page.py',title='Data prediction',icon='🧮')
page6 = streamlit.Page('graph_page.py',title='Data graphics',icon='📉')

streamlit.navigation([main_page,page2,page3,page4,page5,page6]).run()