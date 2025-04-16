import time
import random
from pyrogram.types import Message

EMOJIS = [
    "🦋", "✨", "🌸", "💫", "🌼", "🌙", "🔥", "💎", "⚡",
    "🌪️", "🧿", "💥", "📀", "📼", "💽", "💾", "📂", "📁",
    "🌟", "👑", "🚀", "🎯", "🎉", "🧲", "🎵", "🎶", "🎧",
    "🎷", "🎺", "🎸", "💙", "💚", "💛", "🧡", "❤️", "💜",
    "🧠", "📚", "📝", "✏️", "📖", "📒", "🧃", "🍭", "🍬",
    "🍫", "🍩", "🍪"
]

def human_readable_size(size):
    power = 2 ** 10
    n = 0
    units = ["B", "KiB", "MiB", "GiB", "TiB"]
    while size > power and n < len(units) - 1:
        size /= power
        n += 1
    return f"{round(size, 2)} {units[n]}"

async def progress_bar(current, total, message: Message, start_time, tag="💙Sameer💙"):
    now = time.time()
    elapsed = max(time.time() - start_time, 1)

    speed = current / elapsed
    percentage = current * 100 / total
    eta = (total - current) / speed if speed > 0 else 0

    bar_length = 30
    done = int(bar_length * current / total)
    bar = "█" * done + "▒" * (bar_length - done)

    emoji = random.choice(EMOJIS)  # Random emoji for each update

    progress_text = f"""
{tag}

╔════ ✿ ❀  UPLOADING IN PROGRESS WAIT ✿ ❀ ════╗

➸ 📊 PROGRESS   : [{bar}] {round(percentage, 1)}%
➸ 📶 SPEED      : {human_readable_size(speed)}/s
➸ 📥 DOWNLOADED : {human_readable_size(current)}
➸ 📦 TOTAL SIZE : {human_readable_size(total)}
➸ ⏳ ETA        : {time.strftime('%Mm %Ss', time.gmtime(eta))}

╚════ ✿ ❀ 𝗕𝗬 ➸ @musafir_ji0 ✿ ❀ ════╝

{emoji}  # Random emoji that changes with each update
"""

    try:
        await message.edit_text(f"```{progress_text}```")
    except Exception:
        pass
