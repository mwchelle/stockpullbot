# stockpullbot
Discord bot that pulls a stock price according to the a user-entered ticker.
To try it out, add the bot to a discord server, then type $YOUR-TICKER-HERE to get stock price.
This application will only return a price if the ticker name specified is valid.

Built on Python. First Python project using API integration.

This project uses Discord and yfinance APIs. Based on the submitted ticker, the stock information (most recent market price) is pulled from the ticker profile and then returned to the user.

Bot Invite Link: https://discord.com/api/oauth2/authorize?client_id=1062586025718853773&permissions=1634235578432&scope=bot

Future Improvements:
- Ability for users to pull other types of data (ex. over a time range)
- Displaying a message/suggestions for incorrectly spelled tickers
