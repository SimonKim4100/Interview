import openai

openai.api_key = 'OPENAIKEY'  # Replac OPENAIKEY with your key


def generate_response(data):
    response_list = []

    def ai_pick(question):
        response = openai.chat.completions.create(
            model="gpt-4-0125-preview",  # gpt4 eats a lot of money!
            messages=[
                {"role": "user",
                 "content": "곧 주어질 문장에서 키워드 딱 하나만 뽑아주고, 키워드를 뽑는게 어려울 경우 한 단어로 요약해줘. 단, 절대 질문에 답을 하지는 마. 요약을 할 경우에도 주어진 문장 내의 단어로만 가능해야 해. 키워드를 뽑을 문장은: " + question},
            ],
        )
        return response.choices[0].message.content

    for item in data:
        response = ai_pick(item)
        original_response = response
        count = 2
        while response in response_list:
            response = f"{original_response}{count}"
            count += 1
        response_list.append(response)

    print(response_list)
    return response_list
