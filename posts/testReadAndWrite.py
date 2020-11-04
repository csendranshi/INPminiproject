def EditContent(string):
    new_string=string.replace("'","\\'")
    new_string=new_string.replace("\"","\\\"")
    return new_string

print(EditContent("""
Google has started rolling out a new security update for its Chrome browser on desktops. The new patch includes fixes to a total of 10 bugs in the browser, including a zero-day vulnerability — the second to have been noticed by Google's Threat Analysis Group (TAG) that tracks threat actors in the last two weeks. As always, Google says that details of the bug and links won't be revealed till a majority of Chrome users have installed the update and the vulnerabilities are also fixed in any related third-party library. A zero-day vulnerability refers to a recently discovered software security flaw that could have been already exploited by hackers.

The Google Chrome security patch version  86.0.4240.183 is being released for systems running on Windows, Mac, and Linux. Google in a blog published on the Chrome update on November 2 said that it was aware of reports that an exploit of the particular zero-day vulnerability identified as CVE-2020-16009 exists in the wild. The changelog of the update only has a passing mention that the zero-day bug was in V8 — an open-source JavaScript engine designed for Google Chrome and is also used by other Chromium browsers, such as Microsoft Edge and Opera.

The zero-day issue that the latest patch fixes is the second to be spotted in the last two weeks and the fourth in the last 12 months. Google had last released a security patch on October 20 to fix CVE-2020-15999 — an actively exploited memory corruption bug in the FreeType font rendering library within Chrome. A few days after releasing a security patch to fix it, Google on October 30 revealed that the zero-day CVE-2020-15999 was being exploited in conjunction with a windows zero-day vulnerability identified as CVE-2020-17087. While the malicious code was being executed inside Google Chrome, the Windows zero-day was increasing the code's privileges to attack the Windows OS. Ben Hawkes, the technical lead of Google's Project Zero, an elite team of bug hunters, has said that Microsoft is expected to issue a security patch to fix their security flaw on November 10.

While Google's TAG did not reveal if the two bugs were being exploited by the same threat actors, it confirmed that the motive of the attackers was unrelated to the US presidential elections.
"""))

