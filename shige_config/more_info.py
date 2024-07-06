



# <a href="https://www.patreon.com/Shigeyuki">Patreon : Shigeyuki  Add-ons for gamification</a>


def more_info_text(addon_name, addon_code):
    more_info = """

        <p><strong>[ Related Add-ons ]</strong></p>
            <ul>
            <li><strong><a href="https://ankiweb.net/shared/info/237169833">[ 🔂AnkiRestart ] </a></strong>\
            Quick Aniki Rebooter. Auto restart Anki when progress bar settings are changed.</li>\
            </ul>

        <p><strong>[ Prototype Progress Bars (Patreon) ]</strong></p>
            <ul>
            <li><strong><a href="https://www.patreon.com/posts/how-to-use-bar-1-101346061">[ ProgressBar for Anki ] </a></strong>\
            Review cards are counted in two chunks of progress bars. \
            When the card becomes due the next day or later, it will progress. \
            Calculates each deck and does not reset after restart, and more! </li>\
        <br>
            <li><strong><a href="https://youtu.be/t50NZagCsYk">[ 🎮️AnkiArcade ] </a></strong> \
            Advanced add-on combining mini-games and progress bar. \
            So far it includes 12 mini-game characters, 400+ enemies, 100+ BGMs, ambient sounds, 328 classical music tracks, and more!
            </li>
            </ul>


        <p><strong>[ 🔥Please Support My Activities! ]</strong></p>
        <p>Hi thank you for using this add-on, I'm Shige!😉 I development of Anki Add-ons for Gamification Learning.</p>
        <ul>
            <li><strong><a href="https://new.reddit.com/r/Anki/comments/1b0eybn/simple_fix_of_broken_addons_for_the_latest_anki/">[ 🛠️Fix Add-ons ]</a></strong> So far I fixed 40+ add-ons! You can request simple fixes of broken add-ons from me.</li>
            <li><strong><a href="https://www.patreon.com/Shigeyuki">[ 💖Donation ]</a></strong> You can get all my prototype add-ons for Gamification Learning by becoming a Patron for $5/month. At the moment there are 10 content (add-ons) and 16 themes (AnkiArcade), so only about 20 cents per one.</li>
            <li><strong><a href="https://www.patreon.com/Shigeyuki">[ 🚀Free Supporter  ]</a></strong> When you Free subscribe to Patreon, you will get the latest info, so please check it out!</li>
        </ul>


        <p><b>[ 🛎️Add-on Support ]</b></p>
        If you have any problems or requests, feel free to request them. Thank you!<br>
        <br>
        <a href="https://ankiweb.net/shared/info/{addon_code}">\
        &bull; {addon}</a><br>
        URL : <textarea readonly>https://ankiweb.net/shared/info/{addon_code}</textarea><br>
        Add-on code : <textarea readonly>{addon_code}</textarea> <br>
        <br>
        &bull; <a href="https://ankiweb.net/shared/review/{addon_code}">👍️RateThis : AnkiWeb</a><br>
        <br>
        &bull; <a href="https://www.reddit.com/user/Shige-yuki">👨‍🚀Reddit : u/Shige-yuki </a><br>
        <br>
        &bull; <a href="https://github.com/shigeyukey/my_addons/issues">🐱Github : issues</a><br>
        <br>

        """.format(addon=addon_name, addon_code=addon_code)
    return more_info


