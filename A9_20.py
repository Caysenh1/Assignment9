webpages = ['homepage', 'aboutpage', 'sitemap']
var = list(map(int, input("Enter three values: ").split()))
dict = list(zip(webpages, var))
for i in var:
    if i < 0:
        print("You cannot input negative value(s).")
        var = input("Enter three values: ").split()
        dict = list(zip(webpages, var))
else:
    print(dict)
