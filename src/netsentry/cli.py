# src/netsentry/cli.py
import click
import requests

@click.group()
def cli():
    """NetSentry command-line tool."""
    pass

@cli.command()
@click.option("--url", required=True, help="The URL to check (e.g., https://example.com)")
def check(url):
    """Check if an endpoint is up or down."""
    try:
        response = requests.get(url, timeout=5)
        if response.ok:
            click.echo(f"✅ {url} is UP ({response.status_code})")
        else:
            click.echo(f"⚠️  {url} returned status {response.status_code}")
    except requests.exceptions.RequestException as e:
        click.echo(f"❌ Error checking {url}: {e}")

if __name__ == "__main__":
    cli()
