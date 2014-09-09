Django-popolo-admin
===================
This project aims to add a very simple administration interface to [django-popolo](https://github.com/openpolis/django-popolo).

## Installation

### Clone and install 1st way 
To install you first have to have installed [django-popolo](https://github.com/openpolis/django-popolo) or you could also install [mysociety-django-popolo](https://github.com/mysociety/django-popolo).

Clone this project like `git clone https://github.com/ciudadanointeligente/django-popolo-admin.git` and then cd into it and `python setup.py install`.

### Clone and install 2nd way

Would be installing this using pip: `pip install -e git+git@github.com:ciudadanointeligente/django-popolo-admin.git#egg=popolo_admin`.



In your `INSTALLED_APPS` section in settings.py you have to add `popolo_admin` after `popolo` and it probably is going to look something like:

```
INSTALLED_APPS = (
    ...
    'Django',
    ...

    'popolo',
    ...
    'popolo_admin'
)
```
### Second way
## Testing
I don't have a clue of how to test this. Does anyone do?


## TODOs
- [x] People's admin
- [ ] Organization's admin
- [ ] Post's admin
- [ ] Membership's admin
- [ ] Contact Detail's admin
- [ ] Other name's admin
- [ ] Identifier's admin
- [ ] Link's admin
- [ ] Source's admin
- [ ] Have a easy to follow instructions on how to install
