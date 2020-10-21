# NotHub

NotHub (_working name_) is a simple Notion-GitHub integration built initially to support the development of UBC Launch Pad's [when3meet](https://github.com/ubclaunchpad/when3meet) project.

Currently **(Oct 12 2020)**, this project does one thing only: create a new Notion ticket (on a Notion board of your choice) when a GitHub issue is opened.

The following features are on the roadmap:

- Synchronize issues with page properties, e.g. assignees, labels, etc.
  - [X] Assignees 
  - [ ] Labels
- Move tickets around as GitHub triggers occur (e.g. move the ticket to "Completed" when a PR is merged)

## Getting Started

> TODO: Update this to be more clear

1. Clone the repo
2. Install dependencies
3. Add `.env`
4. Launch the server
5. Connect GitHub

## Why?

As the tech lead for the when3meet project, I needed a way to integrate Notion, which we use internally as a team, and GitHub, which is accessible club-wide.

## How It Works

Under the hood, it uses Jamie Alexander's awesome [notion-py](https://github.com/jamalex/notion-py) library, GitHub webhooks, and a bit of reverse engineering.

Because Notion does not have a public API, this project may break without notice - if it does, consider looking in notion-py's [issues](https://github.com/jamalex/notion-py/issues) page for potential workarounds.
