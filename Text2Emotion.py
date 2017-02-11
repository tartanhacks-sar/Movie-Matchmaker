from watson_developer_cloud import AlchemyLanguageV1

class Text2Emotion(object):

    # bluemix AlchemyApi API key
    api_key = '6487efd8fd5427eec5345d11fa679e3293370dd2'

    def __init__(self):
        # construct API object from key
        self.alchemy_language = AlchemyLanguageV1(api_key=api_key)

    #generates dictionary with emotions as keys and percents as values
    def generate(self, text):
        # get dictionary of data from text
        text_dict = self.alchemy_language.emotion(text = text, language = 'english')
        
        # get dictionary from text_dict
        emotion_dict = text_dict['docEmotions']

        # convert individual emotions percents to floats
        (joy, disgust, anger, fear, sadness) = (float(emotion_dict["joy"]),
                                                float(emotion_dict["disgust"]),
                                                float(emotion_dict["anger"]),
                                                float(emotion_dict["fear"]),
                                                float(emotion_dict["sadness"]))

        # recalculate emotion percents and store them back in emotion_dict as floats
        total = (joy + disgust + anger + fear + sadness)
        emotion_dict["joy"] = joy/total
        emotion_dict["disgust"] = disgust/total
        emotion_dict["anger"] = anger/total
        emotion_dict["fear"] = fear/total
        emotion_dict["sadness"] = sadness/total

        return emotion_dict