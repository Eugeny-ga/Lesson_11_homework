
import json

filename = "candidates.json"

def load_candidates_from_json(filename):
    """Загрузит данные кандидатов из файла json"""

    with open(filename, "r", encoding="utf-8") as file:

        return json.load(file)


def get_all():
    """Покажет всех кандидатов"""
    return load_candidates_from_json(filename)


def get_candidate_by_id(candidate_id):
    """Вернет кандидата по id"""

    for candidate in load_candidates_from_json(filename):
        if candidate["id"] == int(candidate_id):
            return candidate
    return


def get_candidates_by_name(candidate_name):
    """Вернет кандидатов по имени"""
    candidates = []
    for candidate in load_candidates_from_json(filename):
        if candidate_name in candidate["name"]:
            candidates.append(candidate)
    return candidates

def get_candidates_by_skill(skill_name):
    """Вернет кандидатов по навыку"""

    candidates_with_skill = []

    for candidate in load_candidates_from_json(filename):
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            candidates_with_skill.append(candidate)
    return candidates_with_skill

