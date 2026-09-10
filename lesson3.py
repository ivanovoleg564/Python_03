print("Практическое занятие №3")
print("Я изучаю Git")
print("Git помогает сохранять историю проекта")


def приветствие(имя):
    print(f"Привет, {имя}! Работаем с Git.")

приветствие("Студент")



# --- Мини-проект: Моя карточка разработчика ---
name = "Олег"
group = "1-ИИ-2-11-26"
skills = ["Python", "NumPy", "Pandas", "Git"]

print("\n--- Моя карточка разработчика ---")
print("Имя:", name)
print("Группа:", group)
print("Навыки:")
for skill in skills:
    print("-", skill)