"""CreateBlogsTables Migration."""

from masoniteorm.migrations import Migration


class CreateBlogsTables(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("blogs") as table:
            table.increments("id")

            table.timestamps()
            table.string("title")
            table.string("body")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("blogs")
