from openai import OpenAI
import time

client = OpenAI(api_key="")  # Enter your key

assistant = client.beta.assistants.create(
    name="Interviewer",
    instructions="You are an interview assistant. Your job is to find a single keyword from a given sentence. The language of the sentence will be Korean.",
    model="gpt-3.5-turbo-0125"  # Change version accordingly
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Say something here"  # Enter your content, question in this case
)

run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)


def wait_on_run(run, thread):  # Assistant requires some time to be fetched
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run