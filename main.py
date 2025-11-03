from js import document

def compute_average(event=None):
    subjects = ["english", "math", "science", "ss", "filipino", "ict"]
    total = 0

    for subject in subjects:
        val = document.getElementById(subject).value
        val = float(val) if val else 0
        total += val
        document.getElementById(f"{subject}_output").innerText = val

    avg = total / len(subjects)
    first = document.getElementById("first").value
    last = document.getElementById("last").value

    document.getElementById("name").innerText = f"Student: {first} {last}"
    document.getElementById("output").innerText = f"Average grade: {avg:.2f}"
    document.getElementById("grades_container").style.display = "block"