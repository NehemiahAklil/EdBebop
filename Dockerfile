# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
# This file is a part of < https://github.com/TeamUltroid/Ultroid/>
# PLease read the GNU Affero General Public License in <https://www.github.com/NehemiahAklil/EdBebop/blob/main/LICENSE/>.

FROM NehemiahAklil/EdBebop:main

# set timezone
ENV TZ=Africa/AddisAbaba
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/TeamUltroid"

# start the bot.
CMD ["bash", "startup"]
