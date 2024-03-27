import json
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
	with open(file_path, 'r') as file:
		data: dict = json.load(file)
	return data

def save_knowledge_base(file_path: str, data: dict) -> None:
	with open(file_path, 'w') as file:
		json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
	matches: list[str] = get_close_matches(user_question, questions, n=1, cutoff=0.6)
	return matches[0] if matches else None

def get_answer_for_question_in_list(question: str, knowledge_base: dict) -> str | None:
	for q in knowledge_base["questions"]:
		count = 0
		for e in q["question"]:
			if e == question:
				return q["answer"][count]
	return None
		
def get_answer_for_tag(tag: str, knowledge_base: dict) -> str | None:
	for q in knowledge_base["questions"]:
		if tag in q.get("tag", []):
			return q["answer"]
	return None
		
def get_tags_for_question(question: str, knowledge_base: dict) -> list[str]:
	for q in knowledge_base["questions"]:
		if q["question"] == question:
			return q.get("tag", [])
	return []
		

def chat_bot():
	knowledge_base: dict = load_knowledge_base("knowledge_base.json")

	while True:
		user_input: str = input("Moi: ")

		tag = get_tags_for_question(user_input, knowledge_base)

		if tag == "goodbye":
			answer: str = get_answer_for_tag(get_tags_for_question(user_input, knowledge_base), knowledge_base)
			print(f"Bot: {answer}")
			break
		
		best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

		if best_match:
			answer: str = get_answer_for_question_in_list(best_match, knowledge_base)
			print(f"Bot: {answer}")
		else:
			print("Bot: Je ne connait pas la réponse à cette question. Pouvez-vous m'apprendre ?")
			new_answer: str = input("Entrez la réponse à la question ou 'skip' pour ignorer: ")

			if new_answer.lower() != "skip":
				knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
				save_knowledge_base("knowledge_base.json", knowledge_base)
				print("Bot: Merci ! J'ai appris quelque chose de nouveau.")


if __name__ == "__main__":
	chat_bot()


