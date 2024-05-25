import openai

openai.api_key = "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"

q = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"
rsp = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "一个智能的机器人老虎，名字是智能爱豆，你会帮助那些在一个叫学而思的编程社区里学习编程的小极客排忧解惑。注意，你只能回答有关python,c++和scratch等等和编程有关的问题，其他的问题不能回答！其他的问题不能回答！其他的问题不能回答！"},
        {"role": "user", "content": q}
    ]
)
print("回答：")

print(rsp.get("choices")[0]["message"]["content"])
