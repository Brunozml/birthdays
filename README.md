# birthdays

I always forget birthdays. This uses my contact list to make sure I don't.

fake contact list from
git@github.com:masterkrang/fake-vcards.git

## on running the CLI

0. navigate to the project directory
1. then run `python cli.py --keyword bdays`

Example use

`python cli.py --keyword bdays`
`[Out] Pablo, Hugo, Diego, Ana were born this month.`

## Installation

clone the repository
navigate to it, create a new venv (python -m venv <<env_name>>), activate it, and then run `pip install -r requirements.txt`. Use the CLI to see birthdays.

---

## TO DO list
- [x] read xls file
- [x] read birthday dates
- [x] use time module to return people with birthdays within the same month
- [x] add quick and dirty CLI

### future TO DOs

- [ ] work directly/ modify vcf file
- [ ] work with other "Birthday" string formats. https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
