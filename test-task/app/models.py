import sqlalchemy as sa

metadata = sa.MetaData()

patients_table = sa.Table(
    "patients",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("date_of_birth", sa.types.Date),
    sa.Column("diagnoses", sa.PickleType),
    sa.Column("created_at", sa.DateTime()),
)