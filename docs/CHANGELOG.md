# Changelog

## [Unreleased]

### Added
- Simple proof of work consensus algorithm.
- HTTP node server with endpoints for transactions, mining, and chain retrieval.
- Transaction class with JSON serialization and hashing.
- Comprehensive test suite for blockchain, transactions, and proof of work.

### Changed
- Updated import paths to work with PYTHONPATH=./src.
- Added to_dict method to Block class for API serialization.

### Fixed
- Fixed import issues in tests by removing 'src.' prefix.
- Resolved AttributeError in Block serialization by adding to_dict method.

### Complications
- Import path issues when running tests with PYTHONPATH=./src.
- Initial confusion with module structure and relative imports.
- Ensuring transaction and block serialization compatibility. 