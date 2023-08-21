# This is a sample Python script.

# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import openpyxl

# load the files
df = pd.read_excel("Revenue_netflix.xlsx")
df1 = pd.read_excel("subscribers.xlsx")
df2 = pd.read_excel("net_profit.xlsx")
df3 = pd.read_excel("content.xlsx")
df4 = pd.read_excel("netflix_region.xlsx")
df5 = pd.read_excel("movie.xlsx")
df10 = pd.read_csv("netflix_data.csv")
df0 = pd.read_excel("demographics.xlsx")
df13 = pd.read_excel("Penteration.xlsx")
df14 = pd.read_excel("average spent hours.xlsx")
df15 = pd.read_excel("ott_subs.xlsx")
# title
st.title("Data-driven Insights for Netflix's")
# load the image
st.sidebar.image("net.jpg", use_column_width=True)
# Selectbox
list_of_content = ['Netflix History', 'Netflix Overview insights', 'Netflix Revenue', 'Netflix Subscriber',
                   'Net Profit', 'Netflix Subscriber by Region',
                   'Content Spend', 'Best Show by Year', 'Netflix Demographics', 'Netflix Penetration rate',
                   "Average spent hours in Netflix", 'Netflix Statistic', 'Netflix Vs The Competition']
option = st.sidebar.selectbox("Data-driven Insights for Netflix's", list_of_content)
st.sidebar.write('You selected:', option)
# create a button
b = st.sidebar.button('Insight Button')

# EDA
if b:
    if option == 'Netflix History':
        st.write('Netflix is a renowned streaming service that was founded by Reed Hastings and Marc Randolph in '
                 '1997. Initially, it started as a DVD-by-mail rental service, providing customers with a wide '
                 'selection of movies and TV shows. In 2007, Netflix introduced its online streaming platform, '
                 'allowing subscribers to stream content directly to their devices. This move marked a significant '
                 'shift in the industry, leading to a decline in traditional video rental stores. Over the years, '
                 'Netflix focused on expanding its streaming library and producing original content, '
                 'including critically acclaimed series like "House of Cards" and "Stranger Things." Today, '
                 'Netflix is available in over 190 countries and has amassed a vast subscriber base, fundamentally '
                 'transforming how people consume entertainment worldwide.')
    elif option == 'Netflix Revenue':
        fig = px.bar(df, df['Year'], df['Revenue'], text_auto='.2s', title="Netflix Revenue in ($bn)")
        st.plotly_chart(fig)
    elif option == 'Netflix Subscriber':
        fig1 = px.line(df1, df1['Year'], df1['Subscriber'], markers=True, title="Netflix Subscriber in ($M)",
                       text='Subscriber')
        st.plotly_chart(fig1)
    elif option == 'Net Profit':
        fig2 = px.bar(df2, df2['year'], df2['Net Income'], text_auto='.2s', title="Netflix Net Profit in ($mm)")
        st.plotly_chart(fig2)
    elif option == 'Content Spend':
        fig3 = px.bar(df3, df3['Year'], df3['Content Spend'], text_auto='.2s', title="Netflix Content Spend in ($bn)")
        st.plotly_chart(fig3)
    elif option == 'Best Show by Year':
        st.header("Best Movies by Year Netflix")
        st.dataframe(df5)
    elif option == 'Netflix Subscriber by Region':
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots

        fig = make_subplots(rows=2, cols=2, start_cell="bottom-left",
                            subplot_titles=(
                                "Netflix Subscriber by US & Canada", "Netflix Subscriber by Latin America",
                                "Netflix Subscriber by EMEA",
                                "Netflix Subscriber by Asia-Pacific"))

        fig.add_trace(go.Bar(x=df4['Year'], y=df4['US & Canada'], name="US & Canada"),
                      row=1, col=1)

        fig.add_trace(go.Bar(x=df4['Year'], y=df4['Latin America'], name="Latin America"),
                      row=1, col=2)

        fig.add_trace(go.Bar(x=df4['Year'], y=df4['EMEA'], name='EMEA'),
                      row=2, col=1)

        fig.add_trace(go.Bar(x=df4['Year'], y=df4['Asia-Pacific'], name='Asia-Pacific'),
                      row=2, col=2)
        fig.update_layout(title_text="Netflix Subscriber by Region (mm)")
        st.plotly_chart(fig)

    elif option == 'Netflix Overview insights':

        df11 = df10['release_year'].value_counts().reset_index().rename(columns={'index':'count','release_year':'total'})
        fig = px.bar(df11, x='count',y='total', title='Total movies released in Each Year')

        st.plotly_chart(fig)

        df12 = df10['type'].value_counts().reset_index()
        fig = px.pie(df12, values='type', names='count', title='Shows Type',
                     color_discrete_map={'Movie': 'lightcyan',
                                         'TV Show': 'darkblue',
                                         })
        st.plotly_chart(fig)

        df13 = df10['country'].value_counts().reset_index().rename(
            columns={'index': 'country', 'country': 'Total_movies'}).head(10)

        fig = px.treemap(df13, names=df13['country'], parents=["" for _ in df13['country']],
                         values=df13['Total_movies'],
                         title="Top 10 countries where most movies/shows released ")
        st.plotly_chart(fig)

        df14 = df10['rating'].value_counts().reset_index().rename(columns={'index':'count','rating':'total'})
        fig = px.bar(df14, x='count', y='total', title='Movie Ratings Distribution', text_auto=True)
        st.plotly_chart(fig)

        st.text("Most Common  words in Geners")
        x = df10['listed_in'].values
        y = "".join(x)
        wordcloud = WordCloud(background_color='black', colormap='Reds').generate(y)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        st.text("Most Common  words in description")
        x = df10['description'].values
        y = "".join(x)
        wordcloud = WordCloud(background_color='black', colormap='Reds').generate(y)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

        st.text("Most Common  words in cast")
        x = df10['cast'].values
        y = "".join(x)
        wordcloud = WordCloud(background_color='black', colormap='Reds').generate(y)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()


    elif option == 'Netflix Demographics':
        fig = px.pie(df0, values='Percentage Of Users', names='Gender', title='Netflix Demographics',
                     color_discrete_map={'Movie': 'lightcyan',
                                         'TV Show': 'darkblue',
                                         })
        st.plotly_chart(fig)

    elif option == 'Netflix Penetration rate':
        st.write("The penetration rate is one of the best measurements to see how successful Netflix has been in "
                 "individual countries.The penetration rate is the percentage of the relevant total population that "
                 "has purchased a Netflix subscription at least once")
        fig = px.bar(df13, df13['Country'], df13['Penetration Rate'], text_auto='.2s',
                     title="Netflix Penetration rate ($mm)")
        st.plotly_chart(fig)

    elif option == "Average spent hours in Netflix":
        fig = px.line(df14, df14['Year'], df14['Average Daily Time Per Subscriber (Global)'],
                      title="Average Daily Time Per Subscriber (Global)")
        st.plotly_chart(fig)
        st.write("This was due to the COVID-19 pandemic in 2020. People spent much more time in their homes and "
                 "therefore "
                 "consumed more streaming content in general.")

    elif option == 'Netflix Statistic':
        st.write('1.Netflix generated $31.6 billion revenue in 2022, a 6.7% increase on the previous year.')
        st.write("2.In Netflix Movie content is more than Tv Show")
        st.write("3.In 2018  most movie has  released")
        st.write("4.In United States most movie/Tv Show has released")
        st.write('5.Most Movies/Tv shows Has TV-MA Ratings')
        st.write("6.Netflix generated 220.6 million subscriber in 2022, a5% increase on the previous year")
        st.write(
            "7.Netflix made $4.4 billion net profit in 2022, the company’s first decline in net income since 2012.")
        st.write("8.The Europe, Middle East & Africa market surpassed the United States & Canada for subscribers in "
                 "2022.")
        st.write("9.Netflix slightly decreased its content spend in 2022, from $17.7 billion to $16.8 billion.")
        st.write(
            "10.The company reported that its users are 49% women and 51% men.This is extremely balanced for any "
            "streaming platform.")
        st.write("11.Netflix has the highest penetration rate in Australia overall..")

    elif option == "Netflix Vs The Competition":
        st.write("It’s no secret that Netflix now has some serious competition:")
        st.write("1.Disney+")
        st.write("2.HBO Max")
        st.write("3.Hulu")
        st.write("4.Amazon Prime")
        st.write("5.Apple TV Plus")
        st.write("There are tons of streaming platforms available to consumers offering lots of different content. "
                 "And some of these new competitors are backed by massive multi-billion dollar companies.")

        st.write("The truth is that most of Netflix’s competitors just copied their model and used it as a blueprint. "
                 "But the reality is that it worked, and Netflix has struggled to maintain its subscriber value – "
                 "especially because Netflix is more expensive.So the big question is can Netlfix continue to be the "
                 "top dog?Here are the latest Netflix statistics you need to know about their competition.")
        st.write("Netflix Is Losing Subscribers 2022 has not been a good year for Netflix.It’s the first year that "
                 "Netflix has had a downturn in subscribers. Every year prior has been continuous growth for the "
                 "company.Netflix posted a big earnings miss in the first quarter of 2022 as it reported losing 200,"
                 "000 subscribers. Things only got worse in the second quarter of 2022 as Netflix reported another "
                 "loss of 1 million subscribers.")

        st.write("This is the direct opposite of the constant growth the platform wants to see and was expected by "
                 "investors.Market experts weren’t as surprised because of the rise in competition. I mean, "
                 "at some point, they would start to have a looser grip on the market, right?But Netflix isn’t "
                 "backing down.")
        st.write("1..The platform is planning to jumpstart growth by:Creating a new ads-supported")
        st.write(
            "2.ServiceTargeting password sharingA recent study estimated password sharing was costing Netflix $6" "billion in revenue per year.")
        st.write("Crazy, right?We will have to wait and see if it’s enough to stop the "
                 "bleeding.")

        st.write("Netflix Is Becoming Too Expensive.")
        st.write("1.The truth is that Netflix is becoming more and more expensive.")
        st.write("2.The online streaming giant has constantly increased prices since 2011." "When it first launched,"
                 "it was just $7.99 per month.")
        st.write("The premium Netflix subscription, which offers 4 ""screens playing " "simultaneously (a common plan "
                 "for families), "
                 "is $20 per month.Netflix has turned ""from “value for ""money” to a “premium” subscription for most "
                 "users.")
        st.write("The big problem is that Netflix is far more expensive than top competitors:")
        st.write("1.Disney Plus – $8 per month")
        st.write("2.Apple TV Plus – $5 per month")
        st.write("3.Hulu (No Ads) – $13 per month")
        st.write("4.HBO Max (No Ads) – $15 per month")
        st.write("5.Amazon Prime Video – $9 per month")

        st.write(" Netflix Has The “Worst” Content")
        st.write("But the big definer on price is the quality of content.")
        st.write("Here’s the truth:")
        st.write("At the moment, the online streaming market is dominated by series. If you can produce great series "
                 "consistently, you will hold onto your subscribers.")
        st.write("Unfortunately, over the last year, Netflix hasn’t been able to produce enough of them.If you are "
                 "after relevant and binge-worthy series, Netflix’s offerings have only seemed to worsen. Especially "
                 "when you compare it to competitors.")
        st.write("That’s not to say that Netflix has no good shows. But you are paying a premium price for a lot of "
                 "general content. This is directly opposite to a platform like Apple TV Plus, which only offers "
                 "premium content.")
        st.write("think of it like a quantity vs quality situation.")
        st.write("Other streaming platforms like Disney Plus have also focussed on developing their platform content "
                 "offerings.")

        st.write("When it first launched, Disney Plus had a considerable amount of content for children but lacked "
                 "quality content for adults.")
        st.write("But Netflix Still Dominate The Market In Term Of Subscribers (For Now)Even though Netflix declined "
                 "in subscribers – They are still at the top of the streaming market (for now at least).")

        st.dataframe(df15)
