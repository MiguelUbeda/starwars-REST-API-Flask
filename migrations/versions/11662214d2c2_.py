"""empty message

Revision ID: 11662214d2c2
Revises: c96f7a177220
Create Date: 2022-07-28 09:58:03.634599

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '11662214d2c2'
down_revision = 'c96f7a177220'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('genre', sa.String(length=20), nullable=True),
    sa.Column('eyeColor', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=200), nullable=True),
    sa.Column('habitantes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('peopleFav',
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.Column('people_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['people_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('users_id', 'people_id')
    )
    op.create_table('planetsFav',
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.Column('planets_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planets_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('users_id', 'planets_id')
    )
    op.drop_table('planetasFav')
    op.drop_table('planetas')
    op.drop_table('personajesFav')
    op.drop_table('personajes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personajes',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('genero', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('colorPelo', mysql.VARCHAR(length=150), nullable=True),
    sa.Column('colorOjos', mysql.VARCHAR(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('personajesFav',
    sa.Column('users_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('personajes_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['personajes_id'], ['personajes.id'], name='personajesFav_ibfk_1'),
    sa.ForeignKeyConstraint(['users_id'], ['user.id'], name='personajesFav_ibfk_2'),
    sa.PrimaryKeyConstraint('users_id', 'personajes_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('planetas',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('habitantes', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('planetasFav',
    sa.Column('users_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('planetas_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['planetas_id'], ['planetas.id'], name='planetasFav_ibfk_1'),
    sa.ForeignKeyConstraint(['users_id'], ['user.id'], name='planetasFav_ibfk_2'),
    sa.PrimaryKeyConstraint('users_id', 'planetas_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('planetsFav')
    op.drop_table('peopleFav')
    op.drop_table('planets')
    op.drop_table('people')
    # ### end Alembic commands ###