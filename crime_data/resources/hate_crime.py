from webargs.flaskparser import use_args

from crime_data.common import cdemodels, marshmallow_schemas
from crime_data.common.base import CdeResource, tuning_page, cache_for
from crime_data.extensions import DEFAULT_MAX_AGE, DEFAULT_SURROGATE_AGE

# Template
# variable => [bias_name]


def _is_string(col):
    col0 = list(col.base_columns)[0]
    return issubclass(col0.type.python_type, str)


class HateCrimesCountStates(CdeResource):
    schema = False
    def _stringify(self, data):
        # Override stringify function to fit our needs.
        return [dict(r) for r in data]

    # schema = marshmallow_schemas.IncidentCountSchema()

    @use_args(marshmallow_schemas.IncidentViewCountArgs)
    @cache_for(DEFAULT_MAX_AGE, DEFAULT_SURROGATE_AGE)
    @tuning_page
    def get(self, args, state_id=None, state_abbr=None, variable=None):
        self.verify_api_key(args)
        model = cdemodels.HateCrimeCountView(variable, year=args['year'], state_id=state_id, state_abbr=state_abbr)
        results = model.query(args)
        return self.render_response(results.fetchall(), args, self.schema, csv_filename='{}_hate_crime'.format(state_abbr))


class HateCrimesCountAgencies(CdeResource):
    schema = False
    def _stringify(self, data):
        # Override stringify function to fit our needs.
        return [dict(r) for r in data]

    @use_args(marshmallow_schemas.IncidentViewCountArgs)
    @cache_for(DEFAULT_MAX_AGE, DEFAULT_SURROGATE_AGE)
    @tuning_page
    def get(self, args, ori, variable):
        self.verify_api_key(args)
        model = cdemodels.HateCrimeCountView(variable, year=args['year'], ori=ori)
        results = model.query(args)
        return self.render_response(results.fetchall(), args, self.schema)


class HateCrimesCountNational(CdeResource):
    schema = False
    def _stringify(self, data):
        # Override stringify function to fit our needs.
        return [dict(r) for r in data]

    @use_args(marshmallow_schemas.IncidentViewCountArgs)
    @cache_for(DEFAULT_MAX_AGE, DEFAULT_SURROGATE_AGE)
    @tuning_page
    def get(self, args, variable):
        self.verify_api_key(args)
        model = cdemodels.HateCrimeCountView(variable, year=args['year'])
        results = model.query(args)
        return self.render_response(results.fetchall(), args, self.schema, csv_filename='ht_national')


class HateCrimeOffenseSubcounts(CdeResource):
    schema = False
    def _stringify(self, data):
        # Override stringify function to fit our needs.
        return [dict(r) for r in data]

    @use_args(marshmallow_schemas.OffenseCountViewArgs)
    @cache_for(DEFAULT_MAX_AGE, DEFAULT_SURROGATE_AGE)
    @tuning_page
    def get(self, args, variable, state_id=None, state_abbr=None, ori=None):
        self.verify_api_key(args)

        model = cdemodels.OffenseHateCrimeCountView(variable,
                                                    year=args.get('year', None),
                                                    ori=ori,
                                                    offense_name=args.get('offense_name', None),
                                                    explorer_offense=args.get('explorer_offense', None),
                                                    state_id=state_id,
                                                    state_abbr=state_abbr)
        results = model.query(args)
        return self.render_response(results.fetchall(), args, self.schema, csv_filename='ht_suboffense')
