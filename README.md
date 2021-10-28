# Purpose

To update DDNS for namecheap's premiumDNS service on a 24/7 Pi at the location.
https://www.namecheap.com/support/knowledgebase/article.aspx/43/11/how-do-i-set-up-a-host-for-dynamic-dns/

# Usage

## Installation

### Pull from git

- Navigate to `/home/<USERNAME>/cronjobs/`
- `git pull https://github.com/mrdavidoneill/ddns.git`

### Add .env file

- Copy `.EXAMPLEenv` file to `.env`
- Fill in correct values

### Add cronjob entry as specified in file cronjob

- `crontab -e`
- Add entry from file "cronjob" replacing `<USERNAME>`
- verify with `crontab -l`

## Testing

- Check `logs/` folder for server responses
