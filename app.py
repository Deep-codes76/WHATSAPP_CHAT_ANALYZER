# import streamlit as st
# import preprocessor,helper
#
# import matplotlib.pyplot as plt
# import seaborn as sns
# plt.style.use('ggplot')  # or 'fivethirtyeight', 'bmh', 'classic'
# sns.set_theme(style="whitegrid")    # This affects seaborn plots
# sns.set_palette("Set2")  # Try Set1, Set2, pastels, etc.
# plt.rcParams['axes.facecolor'] = '#f9f9f9'  # Background of plots
# plt.rcParams['figure.facecolor'] = '#f9f9f9'  # Background of figure
# plt.rcParams['axes.edgecolor'] = '#dddddd'
# plt.rcParams['grid.color'] = '#eeeeee'
#
#
# st.sidebar.title("Whatsapp Chat Analyzer")
#
# uploaded_file = st.sidebar.file_uploader("Choose a file")
# if uploaded_file is not None:
#     bytes_data = uploaded_file.getvalue()
#     data = bytes_data.decode("utf-8")
#     # st.text(data)
#     df = preprocessor.preprocess(data)
#     st.dataframe(df)
# #
# #     # fetch unique users
#     user_list = df['user'].unique().tolist()
#     user_list.remove('group_notification')
#     user_list.sort()
#     user_list.insert(0,"Overall")
# #
#     selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)
# #
#     if st.sidebar.button("Show Analysis"):
#
# #
# #         # Stats Area
#         num_messages, words, num_media_messages, num_links= helper.fetch_stats(selected_user,df)
#         st.title("Top Statistics")
#         col1, col2, col3, col4 = st.columns(4)
# #
#         with col1:
#             st.header("Total Messages")
#             st.title(num_messages)
#         with col2:
#             st.header("Total Words")
#             st.title(words)
#         with col3:
#             st.header("Media Shared")
#             st.title(num_media_messages)
#         with col4:
#             st.header("Links Shared")
#             st.title(num_links)
#
#         # monthly timeline
#         # st.title("Monthly Timeline")
#         timeline = helper.monthly_timeline(selected_user,df)
#         # fig,ax = plt.subplots()
#         # ax.plot(timeline['time'], timeline['message'],color='green')
#         # plt.xticks(rotation='vertical')
#         # st.pyplot(fig)
#         fig, ax = plt.subplots(figsize=(10, 4))
#         ax.plot(timeline['time'], timeline['message'], color='green', linewidth=2, marker='o')
#         ax.set_title("Monthly Messages", fontsize=14)
#         ax.set_xlabel("Time", fontsize=12)
#         ax.set_ylabel("Messages", fontsize=12)
#         plt.xticks(rotation=45)
#         plt.tight_layout()
#         st.pyplot(fig)
#
#         # daily timeline
#         st.title("Daily Timeline")
#         daily_timeline = helper.daily_timeline(selected_user, df)
#         fig, ax = plt.subplots()
#         ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
#         plt.xticks(rotation='vertical')
#         st.pyplot(fig)
#
#         # activity map
#         st.title('Activity Map')
#         col1,col2 = st.columns(2)
#
#         with col1:
#             st.header("Most busy day")
#             busy_day = helper.week_activity_map(selected_user,df)
#             fig,ax = plt.subplots()
#             ax.bar(busy_day.index,busy_day.values,color='purple')
#             plt.xticks(rotation='vertical')
#             st.pyplot(fig)
#
#         with col2:
#             st.header("Most busy month")
#             busy_month = helper.month_activity_map(selected_user, df)
#             fig, ax = plt.subplots()
#             ax.bar(busy_month.index, busy_month.values,color='orange')
#             plt.xticks(rotation='vertical')
#             st.pyplot(fig)
#
#         st.title("Weekly Activity Map")
#         user_heatmap = helper.activity_heatmap(selected_user,df)
#         fig,ax = plt.subplots()
#         ax = sns.heatmap(user_heatmap)
#         st.pyplot(fig)
#
# #         # finding the busiest users in the group(Group level)
#         if selected_user == 'Overall':
#             st.title('Most Busy Users')
#             x,new_df = helper.most_busy_users(df)
#             fig, ax = plt.subplots()
#
#             col1, col2 = st.columns(2)
#
#             with col1:
#                 # ax.bar(x.index, x.values,color='red')
#                 # plt.xticks(rotation='vertical')
#                 # st.pyplot(fig)
#                 fig, ax = plt.subplots(figsize=(8, 4))
#                 ax.bar(x.index, x.values, color='tomato', edgecolor='black')
#                 ax.set_title("Most Active Users", fontsize=14)
#                 ax.set_ylabel("Messages", fontsize=12)
#                 plt.xticks(rotation=45)
#                 plt.tight_layout()
#                 st.pyplot(fig)
#
#             with col2:
#                 st.dataframe(new_df)
#
# #         # WordCloud
#         st.title("Wordcloud")
#         df_wc = helper.create_wordcloud(selected_user,df)
#         fig,ax = plt.subplots()
#         ax.imshow(df_wc)
#         st.pyplot(fig)
# #
# #         # most common words
#         most_common_df = helper.most_common_words(selected_user,df)
#
#         fig,ax = plt.subplots()
#
#         ax.barh(most_common_df[0],most_common_df[1])
#         plt.xticks(rotation='vertical')
#
#         st.title('Most common words')
#         st.pyplot(fig)
# #
# #         # emoji analysis
#         emoji_df = helper.emoji_helper(selected_user,df)
#         st.title("Emoji Analysis")
#
#         col1,col2 = st.columns(2)
#
#         with col1:
#             st.dataframe(emoji_df)
#         with col2:
#             fig,ax = plt.subplots()
#             ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f")
#             st.pyplot(fig)
#
#
#
#
#
#
#
#
#
#
# ------------------------beautified code-------------------------------------------
import streamlit as st
import preprocessor, helper

import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')  # or 'fivethirtyeight', 'bmh', 'classic'
sns.set_theme(style="whitegrid")  # This affects seaborn plots
sns.set_palette("Set2")  # Try Set1, Set2, pastels, etc.

# Light plot backgrounds but white text
plt.rcParams.update({
    'axes.facecolor': 'none',
    'figure.facecolor': 'none',
    'axes.edgecolor': '#dddddd',
    'grid.color': '#444444',
    'text.color': 'white',
    'axes.labelcolor': 'white',
    'xtick.color': 'white',
    'ytick.color': 'white',
    'axes.titlecolor': 'white',
    'figure.autolayout': True
})

st.sidebar.title("Whatsapp Chat Analyzer")
st.markdown(
    """
    <h2 style='text-align: center; color: white;'>WELCOME TO THE WHATSAPP CHAT ANALYSIS APP</h2>
    <p style='text-align: center; color: white; font-size: 16px;'>
    BY DEEPANSHU, HERE YOU CAN ANALYZE YOUR WHATSAPP CHATS...<br>
    FEEL FREE TO USE IT 😊
    </p>
    <p style='text-align: center; color: lightgray; font-size: 15px;'>
    🌐 Connect with me on 
    <a href='https://www.linkedin.com/in/deepanshu-kumar-4412b02bb?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app' target='_blank' style='color: #0e76a8; text-decoration: none;'>
    LinkedIn</a>
    </p>
    <p style='text-align: center; color: lightgray; font-size: 15px;'>
    🌐 my github repo --U WILL FIND THE CODE HERE--
    <a href='https://github.com/Deep-codes76' target='_blank' style='color: #0e76a8; text-decoration: none;'>
    GITHUB</a>
    </p>
    """,
    unsafe_allow_html=True
)
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file:
    st.empty()  # This will remove the welcome message
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)
#
#     # fetch unique users
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
#
    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)
#
    if st.sidebar.button("Show Analysis"):

#
#         # Stats Area
        num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)
        st.title("Top Statistics")
        col1, col2, col3, col4 = st.columns(4)
#
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        # monthly timeline
        # st.title("Monthly Timeline")
        timeline = helper.monthly_timeline(selected_user, df)
        # fig,ax = plt.subplots()
        # ax.plot(timeline['time'], timeline['message'],color='green')
        # plt.xticks(rotation='vertical')
        # st.pyplot(fig)
        fig, ax = plt.subplots(figsize=(10, 4), facecolor='none')
        ax.set_facecolor('none')
        ax.plot(timeline['time'], timeline['message'], color='green', linewidth=2, marker='o')
        ax.set_title("Monthly Messages", fontsize=14, color='white')
        ax.set_xlabel("Time", fontsize=12, color='white')
        ax.set_ylabel("Messages", fontsize=12, color='white')
        ax.tick_params(colors='white')
        plt.xticks(rotation=45)
        st.pyplot(fig)

                # daily timeline
        # daily timeline
        st.title("Daily Timeline")
        daily_timeline = helper.daily_timeline(selected_user, df)
        fig, ax = plt.subplots(facecolor='none')
        ax.set_facecolor('none')
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='deepskyblue')  # Changed color
        ax.set_title("Daily Messages", fontsize=14, color='white')
        ax.set_xlabel("Date", fontsize=12, color='white')
        ax.set_ylabel("Messages", fontsize=12, color='white')
        ax.tick_params(colors='white')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)


# activity map
        st.title('Activity Map')
        col1, col2 = st.columns(2)

        with col1:
            st.header("Most busy day")
            busy_day = helper.week_activity_map(selected_user, df)
            fig, ax = plt.subplots(facecolor='none')
            ax.set_facecolor('none')
            ax.bar(busy_day.index, busy_day.values, color='purple')
            ax.set_title("Busy Days", color='white')
            ax.tick_params(colors='white')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most busy month")
            busy_month = helper.month_activity_map(selected_user, df)
            fig, ax = plt.subplots(facecolor='none')
            ax.set_facecolor('none')
            ax.bar(busy_month.index, busy_month.values, color='orange')
            ax.set_title("Busy Months", color='white')
            ax.tick_params(colors='white')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots(facecolor='none')
        ax.set_facecolor('none')
        sns.heatmap(user_heatmap, ax=ax, cmap="YlGnBu", linewidths=0.3, linecolor='gray', cbar=True)
        ax.set_title("Heatmap", color='white')
        ax.tick_params(colors='white')
        st.pyplot(fig)

#         # finding the busiest users in the group(Group level)
        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_users(df)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                # ax.bar(x.index, x.values,color='red')
                # plt.xticks(rotation='vertical')
                # st.pyplot(fig)
                fig, ax = plt.subplots(figsize=(8, 4), facecolor='none')
                ax.set_facecolor('none')
                ax.bar(x.index, x.values, color='tomato', edgecolor='black')
                ax.set_title("Most Active Users", fontsize=14, color='white')
                ax.set_ylabel("Messages", fontsize=12, color='white')
                ax.tick_params(colors='white')
                plt.xticks(rotation=45)
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

#         # WordCloud
        st.title("Wordcloud")
        df_wc = helper.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots(facecolor='none')
        ax.set_facecolor('none')
        ax.imshow(df_wc)
        ax.axis("off")
        st.pyplot(fig)

#
#         # most common words
        most_common_df = helper.most_common_words(selected_user, df)

        fig, ax = plt.subplots(facecolor='none')
        ax.set_facecolor('none')
        ax.barh(most_common_df[0], most_common_df[1])
        ax.set_title("Most Common Words", color='white')
        ax.tick_params(colors='white')
        plt.xticks(rotation='vertical')
        st.title('Most common words')
        st.pyplot(fig)

#
#         # emoji analysis
        emoji_df = helper.emoji_helper(selected_user, df)
        st.title("Emoji Analysis")

        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig, ax = plt.subplots(facecolor='none')
            ax.set_facecolor('none')
            ax.pie(emoji_df[1].head(), labels=emoji_df[0].head(), autopct="%0.2f", textprops={'color': "white"})
            st.pyplot(fig)
