from newsapi.newsapi_client import NewsApiClient

def get_cnn_news(): 

    newsapi = NewsApiClient(api_key='ff705166e5c34413962cabd6d1b3d66f')

    top_headlines = newsapi.get_top_headlines(sources='cnn')
    # print(top_headlines)
    
    news_data = {} ### create dictionary naming as 'news_data'


    news_data['title'] = str(top_headlines['articles'][0]['title']).replace("\\"," ")
    news_data['description'] = str(top_headlines['articles'][0]['description']).replace("\\"," ")
    news_data['url'] = str(top_headlines['articles'][0]['url'])
    news_data['image_url'] = str(top_headlines['articles'][0]['urlToImage'])


    return news_data

# if __name__ == "__main__":
#     news = get_cnn_news()
#     # print('title is ' + news['title']) ## title
#     # print('description is ' + news['description']) ## description
#     # print('url is ' +news[2]) ## url
#     print(news['description'])



