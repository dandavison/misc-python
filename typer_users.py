import typer

app = typer.Typer()


@app.command()
def create(user_name: str):
    print(f"Creating user: {user_name}")


@app.command()
def delete(user_name: str):
    print(f"Deleting user: {user_name}")


@app.callback(invoke_without_command=True)
def cb(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        print("No subcommand was invoked...")
        ctx.invoke(create, user_name="John Doe")
    else:
        print(f"Subcommand '{ctx.invoked_subcommand}' was invoked")


if __name__ == "__main__":
    app()
