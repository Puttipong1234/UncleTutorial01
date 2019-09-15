def get_cnn_news(): 
    from newsapi import NewsApiClient

    newsapi = NewsApiClient(api_key='ff705166e5c34413962cabd6d1b3d66f')

    top_headlines = newsapi.get_top_headlines(sources='cnn')
    print(top_headlines)

    title = top_headlines['articles'][0]['title']
    description = top_headlines['articles'][0]['description']
    url = top_headlines['articles'][0]['url']
    return title , description , url
