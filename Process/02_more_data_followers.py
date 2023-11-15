from bs4 import BeautifulSoup

html_code = """
<div class="x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><div class="x9f619 x1n2onr6 x1ja2u2z x1qjc9v5 x78zum5 xdt5ytf x1iyjqo2 xl56j7k xeuugli"><div class="x9f619 x1n2onr6 x1ja2u2z x78zum5 x2lah0s x1qughib x6s0dn4 xozqiw3 x1q0g3np"><div class="x9f619 x1n2onr6 x1ja2u2z xdt5ytf x2lah0s x193iq5w xeuugli xamitd3 x78zum5"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xq8finb x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><div class=""><div><div class="_aarf _aarg" aria-disabled="false" role="button" tabindex="0" style="cursor: pointer;"><canvas class="_aarh" height="54" width="54" style="left: -5px; position: absolute; top: -5px; height: 54px; width: 54px;"></canvas><span class="xnz67gz x14yjl9h xudhj91 x18nykt9 xww2gxu x9f619 x1lliihq x2lah0s x6ikm8r x10wlt62 x1n2onr6 xzfakq x7imw91 x1j8hi7x x5aw536 x194ut8o x1vzenxt xd7ygy7 xt298gk xynf4tj xdspwft x1r9ni5o x1d52zm6 xoiy6we x15xhmf9 x1qj619r x15tem40 x1xrz1ek x1s928wv x1n449xj x2q1x1w x1j6awrg x162n7g1 x1m1drc7" role="link" tabindex="-1" style="height: 44px; width: 44px;"><img alt="ovi_garudacyber's profile picture" class="xpdipgo x972fbf xcfux6l x1qhh985 xm0m39n xk390pu x5yr21d xdj266r x11i5rnm xat24cr x1mh8g0r xl1xv1r xexx8yu x4uap5 x18d9i69 xkhd6sd x11njtxf xh8yej3" crossorigin="anonymous" draggable="false" src="https://instagram.fjog3-1.fna.fbcdn.net/v/t51.2885-19/374193990_286756137433079_7086426022721467431_n.jpg?stp=dst-jpg_s150x150&amp;_nc_ht=instagram.fjog3-1.fna.fbcdn.net&amp;_nc_cat=111&amp;_nc_ohc=7P25P3WU8t4AX-1Ka1p&amp;edm=APQMUHMBAAAA&amp;ccb=7-5&amp;oh=00_AfC-sByi6EpoDING1oUBpxE_nQEKcFH_0PshTgqer48b6g&amp;oe=6558EAFE&amp;_nc_sid=6ff7c8"></span></div></div></div></div></div><div class="x9f619 x1n2onr6 x1ja2u2z x78zum5 x1iyjqo2 xs83m0k xeuugli x1qughib x6s0dn4 x1a02dak x1q0g3np xdl72j9"><div class="x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w xeuugli x1iyjqo2"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><div class="x1rg5ohu"><div><a class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz notranslate _a6hd" href="/ovi_garudacyber/" role="link" tabindex="0"><div class="x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1"><span class="_ap3a _aaco _aacw _aacx _aad7 _aade" dir="auto">ovi_garudacyber</span></div></div></a></div></div><div class="x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x150jy0e x1e558r4 x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1">·</div><button class=" _acan _acao _acas _aj1- _ap30" type="button"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x4uap5 xkhd6sd x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh xl56j7k" style="height: 100%;"><div class="_ap3a _aacn _aacw _aad6" dir="auto">Follow</div></div></button></div><span class="x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x1roi4f4 x10wh9bi x1wdrske x8viiok x18hxmgj" dir="auto" style="line-height: var(--base-line-clamp-line-height); --base-line-clamp-line-height: 18px;"><span class="x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft">Marketing Garuda Cyber Indonesia</span></span></div></div></div><div class="x9f619 x1n2onr6 x1ja2u2z xdt5ytf x2lah0s x193iq5w xeuugli xamitd3 x78zum5"><div class="x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x16n37ib x1uhb9sk x1plvlek xryxfnj x1c4vz4f xs83m0k x1q0g3np xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1"><div class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x78zum5 x1f6kntn xwhw2v2 x10w6t97 xl56j7k x17ydfre x1swvt13 x1pi30zi x1n2onr6 x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye x1gjpkn9 x5n08af xsz8vos" role="button" tabindex="0">Remove</div></div></div></div></div></div></div>
"""

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')

# Find all the div blocks containing user information
user_divs = soup.find_all('div', class_='x9f619')

# Loop through each user div
for user_div in user_divs:
    # Extract profile picture information
    profile_picture_alt = user_div.find('img', class_='xpdipgo')['alt']

    # Extract username information
    username = user_div.find('span', class_='_ap3a').text

    # Extract URL of the profile picture
    profile_picture_url = user_div.find('img', draggable='false')['src']

    # Extract name information
    name = user_div.find('span', class_='x1lliihq').text

    # Print the results for each set of data
    print(f"{username}'s profile picture")
    print(f"username: {username}")
    print(f"url profile picture: {profile_picture_url}")
    print(f"name: {name}")
    print("------")
