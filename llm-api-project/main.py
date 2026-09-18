from llm_api import send_post_request


def main():
	prompt = input("Enter a prompt: ")
	response = send_post_request(prompt)
	print(response)


if __name__ == "__main__":
	main()
