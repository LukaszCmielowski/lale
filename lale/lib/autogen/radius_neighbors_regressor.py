
from sklearn.neighbors.regression import RadiusNeighborsRegressor as SKLModel
import lale.helpers
import lale.operators
from numpy import nan, inf

class RadiusNeighborsRegressorImpl():

    def __init__(self, radius=1.0, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=None):
        self._hyperparams = {
            'radius': radius,
            'weights': weights,
            'algorithm': algorithm,
            'leaf_size': leaf_size,
            'p': p,
            'metric': metric,
            'metric_params': metric_params,
            'n_jobs': n_jobs}

    def fit(self, X, y=None):
        self._sklearn_model = SKLModel(**self._hyperparams)
        if (y is not None):
            self._sklearn_model.fit(X, y)
        else:
            self._sklearn_model.fit(X)
        return self

    def predict(self, X):
        return self._sklearn_model.predict(X)
_hyperparams_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'inherited docstring for RadiusNeighborsRegressor    Regression based on neighbors within a fixed radius.',
    'allOf': [{
        'type': 'object',
        'relevantToOptimizer': ['weights', 'algorithm', 'leaf_size', 'p', 'metric'],
        'additionalProperties': False,
        'properties': {
            'radius': {
                'type': 'number',
                'default': 1.0,
                'description': 'Range of parameter space to use by default for :meth:`radius_neighbors`'},
            'weights': {
                'anyOf': [{
                    'type': 'object',
                    'forOptimizer': False}, {
                    'enum': ['distance', 'uniform']}],
                'default': 'uniform',
                'description': 'weight function used in prediction.  Possible values:'},
            'algorithm': {
                'enum': ['auto', 'ball_tree', 'kd_tree', 'brute'],
                'default': 'auto',
                'description': 'Algorithm used to compute the nearest neighbors:'},
            'leaf_size': {
                'type': 'integer',
                'minimumForOptimizer': 30,
                'maximumForOptimizer': 31,
                'distribution': 'uniform',
                'default': 30,
                'description': 'Leaf size passed to BallTree or KDTree.  This can affect the'},
            'p': {
                'type': 'integer',
                'minimumForOptimizer': 2,
                'maximumForOptimizer': 3,
                'distribution': 'uniform',
                'default': 2,
                'description': 'Power parameter for the Minkowski metric. When p = 1, this is'},
            'metric': {
                'anyOf': [{
                    'type': 'object',
                    'forOptimizer': False}, {
                    'enum': ['euclidean', 'manhattan', 'minkowski', 'precomputed']}],
                'default': 'minkowski',
                'description': 'the distance metric to use for the tree.  The default metric is'},
            'metric_params': {
                'anyOf': [{
                    'type': 'object'}, {
                    'enum': [None]}],
                'default': None,
                'description': 'Additional keyword arguments for the metric function.'},
            'n_jobs': {
                'anyOf': [{
                    'type': 'integer'}, {
                    'enum': [None]}],
                'default': None,
                'description': 'The number of parallel jobs to run for neighbors search.'},
        }}],
}
_input_fit_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Fit the model using X as training data and y as target values',
    'type': 'object',
    'properties': {
        'X': {
            'type': 'array',
            'items': {
                'XXX TODO XXX': 'item type'},
            'XXX TODO XXX': '{array-like, sparse matrix, BallTree, KDTree}',
            'description': 'Training data. If array or matrix, shape [n_samples, n_features],'},
        'y': {
            'type': 'array',
            'items': {
                'XXX TODO XXX': 'item type'},
            'XXX TODO XXX': '{array-like, sparse matrix}',
            'description': 'Target values, array of float values, shape = [n_samples]'},
    },
}
_input_predict_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Predict the target for the provided data',
    'type': 'object',
    'properties': {
        'X': {
            'XXX TODO XXX': "array-like, shape (n_query, n_features),                 or (n_query, n_indexed) if metric == 'precomputed'",
            'description': 'Test samples.'},
    },
}
_output_predict_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Target values',
    'XXX TODO XXX': 'array of float, shape = [n_samples] or [n_samples, n_outputs]',
}
_combined_schemas = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Combined schema for expected data and hyperparameters.',
    'type': 'object',
    'tags': {
        'pre': [],
        'op': ['estimator'],
        'post': []},
    'properties': {
        'hyperparams': _hyperparams_schema,
        'input_fit': _input_fit_schema,
        'input_predict': _input_predict_schema,
        'output_predict': _output_predict_schema},
}
if (__name__ == '__main__'):
    lale.helpers.validate_is_schema(_combined_schemas)
RadiusNeighborsRegressor = lale.operators.make_operator(RadiusNeighborsRegressorImpl, _combined_schemas)
