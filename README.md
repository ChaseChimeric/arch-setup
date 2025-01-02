The purpose of this repo is to streamline installing arch with most of my personal preferences.
This can also be used as a quick start for other newer users

to use this repo, follow the [arch installation guide](https://wiki.archlinux.org/title/Installation_guide)
**After completing step 3.2**, continue here by running the following
```curl -sS https://pastebin.com/raw/50H3L4dF | bash```


quick note,
for the reasoning about why I didn't automate the steps before 3.2 in the guide, I mainly wanted to leave the partitioning and drive formatting out of automation so that it can be made more custom depending on the use. because of this I also didn't enable os-prober for GRUB since if you're dual booting then you can enable it yourself.
