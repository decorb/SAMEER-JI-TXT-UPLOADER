import time
import random
from pyrogram.types import Message

# One emoji only
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
    if elapsed == 0:
        elapsed = 1

    speed = current / elapsed
    percentage = current * 100 / total
    eta = (total - current) / speed if speed > 0 else 0

    bar_length = 30
    done = int(bar_length * current / total)
    bar = "█" * done + "▒" * (bar_length - done)

    emoji = random.choice(EMOJIS)

    progress_text = f"""
╭━━━━━⭑ 𝗨𝗣𝗟𝗢𝗔𝗗 𝗜𝗡 𝗣𝗥𝗢𝗚𝗥𝗘𝗦𝗦 ⭑━━━━━╮

📶 SPEED     : {human_readable_size(speed)}/s
📊 PROGRESS  : [{bar}] {round(percentage, 1)}%
📥 DOWNLOADED: {human_readable_size(current)}
📦 TOTAL SIZE: {human_readable_size(total)}
⏳ ETA       : {time.strftime('%Mm %Ss', time.gmtime(eta))}

╰━━➤ 𝗠𝗔𝗗𝗘 𝗪𝗜𝗧𝗛 💙 𝗕𝗬 ➤ @musafir_ji0

{tag} {emoji}
"""

    try:
        await message.edit_text(f"```{progress_text}```")
    except Exception:
        pass
