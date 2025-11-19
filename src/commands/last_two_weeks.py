import discord

from services import googleCalendarService, googleAuth

async def last_two_weeks(message: discord.Message):
    await message.channel.send("Fetching events from the last two weeks...")

    credentials = googleAuth.get_credentials()
    events = googleCalendarService.get_lastTwoWeeksEvents(credentials)

    if not events:
        await message.channel.send("No events found in the last two weeks.")
        return


    chunk_size = 25
    for i in range(0, len(events), chunk_size):
        chunk = events[i:i + chunk_size]

        embed = discord.Embed(
            title="Events From the Last Two Weeks",
            description=f"Events {i + 1}–{i + len(chunk)} of {len(events)}",
            color=0x2ecc71,  
        )

        for event in chunk:
            start = event["start"].get("dateTime", event["start"].get("date"))
            end = event["end"].get("dateTime", event["end"].get("date"))
            summary = event.get("summary", "(no title)")

            embed.add_field(
                name=summary,
                value=f"{start} → {end}",
                inline=False,
            )
        await message.channel.send(embed=embed)

        