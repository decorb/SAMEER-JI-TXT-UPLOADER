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
    elapsed = now - start_time
    elapsed = elapsed if elapsed > 0 else 1

    speed = current / elapsed
    percentage = current * 100 / total
    eta = (total - current) / speed if speed > 0 else 0

    bar_length = 30
    done = int(bar_length * current / total)
    bar = "█" * done + "▒" * (bar_length - done)

    emoji = random.choice(EMOJIS)

    progress_text = f"""
UPLOAD IN PROGRESS...

Speed       : {human_readable_size(speed)}/s
Progress    : [{bar}] {round(percentage, 1)}%
Downloaded  : {human_readable_size(current)}
Total Size  : {human_readable_size(total)}
ETA         : {time.strftime('%Mm %Ss', time.gmtime(eta))}

Made by @musafir_ji0
{tag}
{emoji}
"""

    try:
        await message.edit_text(f"```{progress_text}```")
    except Exception:
        pass
