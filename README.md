# Designing a URL Shortening Service

  *URL* Shortening will be used to create a shorter alianse for long _URLs_. We call it _Short Links_ where users are 
redirected to the original _URL_ when they hit the short links buttob lik this ....

  URL shortening is used for optimizing links across devices, tracking individual links to analyze 
audience and campaign performance, and hiding affiliated original URLs.


##  Requirements and Goals of the System

_Our URL shortening system should meet the following requirements_

__Fuctional Requirements :__
1. Given a _URL_, our services should generate a shorter alias _URL_.

2. When users access a short link, our service should redirect them to the original link.

3. Users have the optionallity to be able to pick a custom link for thier _URL_ .

4. Links will expire after a standard timespan. Users should specify that expiration time.

## System APIs ..
Following could be the definitions of the APIs for creating and deleting URLs:  
 > createURL( original_url, custom_alias=None, user_name=None,
expire_date=None)
__Parameters:__ 
  - `original_url (string)`: Original URL to be shortened.
  - `custom_alias (string)`: Optional custom key for the URL.
  - `user_name (string)`: Optional user name to be used in encoding.
  - `expire_date (string)`: Optional expiration date for the shortened URL.

__Returns: (string)__ 
  - _A successful insertion returns the shortened URL; otherwise, it returns an error code._ 

> deleteURL(url_key)
__Parameters:__ 
  -  `“url_key”` is a string representing the shortened URL to be retrieved. A successful deletion 
__Returns__ 
  - ‘URL Removed’ and to redirect users to the home page. 

---
 __How do we detect and prevent abuse?__

 > Abuse would happen if amalicious user comsume all _URL_ keys. And to preven such abuse, we can limit users via thier `api_dev_key` where each `api_dev_key` can be limited to a certain number of _URLs_ whither for creations or redirections per some given time period.

 ## DataBase Design ..

 __Database Schema:__
 
 We would need two tables: 
  - One for storing information about the URL mappings
  - And one for the user’s data who created the short link.

> For now we only focus on the __Link__ Table only.

## Basic System Design and Algorithm..

we are solving here is, how to generate a short and unique key for a given URL, the question can be simplified like this – given a URL, how can we find hash function F that maps URL to a short alias:
`F(URL) = alias`
and satisfies following conditions:

- Each URL can only be mapped to a unique alias
- Each alias can be mapped back to a unique URL easily
- The second condition is the core as in the run time, the system should look up by alias and redirect to the corresponding URL quickly.

## Installed Packages

On running this command 
```
pip freeze > requirements.txt
```
we got this [requirements.txt](https://github.com/Rowida46/URL-Shortening-Service/blob/main/requirements.txt) File