# Normalized Bijankhan Corpus

[Bijankhan](https://en.wikipedia.org/wiki/Bijankhan_Corpus) is a large tagged corpus in Persian language. Unfortunately this corpus is not in utf-8 format and also has a lot of misspelled words.
I tried to normalized Bijankhan corpus by some simple replacements.

**موارد اصلاح شده:**
- تبدیل حروف عربی به معادل فارسی
- در برخی از کلمات فاصله و نیم فاصله در کنار هم قرار گرفته‌اند
- به دلیل نامشخصی برخی کلمات دارای همزه به اشتباه وارد دادگان شده‌اند. برای مثال مطمان، ارااه، مساال، تااتر و [بیشتر](./misspelled.txt)


## How to run
Simply run the `bijankhan.py` to normalize the corpus. for help type 'python bijankhan.py -h'


## Supporting Tihu
If you like this project, please [donate](http://lilak-project.com/donate.php) or consider becoming a patron:

[![Become a patron](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://patreon.com/b00f)


## License
Using/modifing this script has no limitation due to its license (GNU v3.0).
But if you like to use Bijankhan corpus you need to contact to the [owner](http://dbrg.ut.ac.ir/Bijankhan/).
