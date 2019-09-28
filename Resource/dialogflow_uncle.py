import dialogflow
import os
def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)
        data = {}
        data['fulfillment_text'] = response.query_result.fulfillment_text
        data['respones'] = response
        data['parameters'] = response.query_result.parameters
        return data

# if __name__ == "__main__":
#     ### enable google dialogflow api
#     ### firstly set GOOGLE_APPLICATION_CREDENTIALS=Credentials.json
#     i = 0
#     while(i<5):
#         message = input('please input some text :')
#         project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
#         res = detect_intent_texts(project_id, "1234", message, 'th')

#         print(res)
#         i += 1