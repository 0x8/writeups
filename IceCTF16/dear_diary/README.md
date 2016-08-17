#Nullp0inter's dear_diary write up for IceCTF 2016

##Dear_Diary Pwn 60pts
We all want to keep our secrets secure and what is more important than our
precious diary entries? We made this highly secure diary service that is
sure to keep all your boy crushes and edgy poems safe from your parents. 
nc diary.vuln.icec.tf 6501

## Write Up
In this challenge we are given a download link for a elf-32bit binary. The
idea is that this binary acts as a diary of sorts, allowing you to write an

```
-- Diary 3000 --

1. add entry
2. print latest entry
3. quit
> 
```


Thats a bit odd for a diary, just one entry. After playing around a little
bit process of elemination shows the program does not allow specifically "n",
that is to say the lowercase (uppercase is fine), which is undoubtedly also
strange behavior. My mind is already screaming Format String Vulnerability
but just to verify I tried to enter 'AAAA%x%x%x%x%x%x%x' as an entry and
print it:
```
-- Diary 3000 --

1. add entry
2. print latest entry
3. quit
> 1
Tell me all your secrets: AAAA%x%x%x%x%x%x%x

1. add entry
2. print latest entry
3. quit
> 2
AAAA6ef757eed5fff4d948fff4ed480a8c521f00

1. add entry
2. print latest entry
3. quit
> 
```

Clearly its not handling format strings properly according to the output above.
This is good for us
