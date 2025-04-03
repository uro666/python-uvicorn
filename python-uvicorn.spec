%define module uvicorn
# disable test on abf
%bcond_with test

Name:		python-uvicorn
Version:	0.34.0
Release:	1
Summary:	An ASGI web server, for Python
URL:		https://www.uvicorn.org/
License:	BSD-3-Clause
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/u/uvicorn/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(a2wsgi)
BuildRequires:	python%{pyver}dist(build)
BuildRequires:	python%{pyver}dist(click)
BuildRequires:	python%{pyver}dist(cryptography)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(h11)
BuildRequires:	python%{pyver}dist(httpx)
BuildRequires:	python%{pyver}dist(trustme)
BuildRequires:	python%{pyver}dist(twine)
BuildRequires:	python%{pyver}dist(typing-extensions)
BuildRequires:	python%{pyver}dist(wsproto)
BuildRequires:	python%{pyver}dist(websockets)
# Optionals
BuildRequires:	python%{pyver}dist(colorama)
BuildRequires:	python%{pyver}dist(httptools)
BuildRequires:	python%{pyver}dist(python-dotenv)
BuildRequires:	python%{pyver}dist(pyyaml)
BuildRequires:	python%{pyver}dist(uvloop)
BuildRequires:	python%{pyver}dist(watchfiles)

%if %{with test}
BuildRequires:	python%{pyver}dist(coverage)
BuildRequires:	python%{pyver}dist(coverage-conditional-plugin)
BuildRequires:	python%{pyver}dist(mypy)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-mock)
BuildRequires:	python%{pyver}dist(ruff)
BuildRequires:	python%{pyver}dist(types-click)
BuildRequires:	python%{pyver}dist(types-pyyaml)
%endif

Recommends:     python-PyYAML >= 5.1
Recommends:     python-httptools >= 0.6.3
Recommends:     python-websockets >= 10.4
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description
Uvicorn is an ASGI web server implementation for Python.

Until recently Python has lacked a minimal low-level server/application
interface for async frameworks. The ASGI specification fills this gap,
and means we're now able to start building a common set of tooling usable
across all async frameworks.

Uvicorn supports HTTP/1.1 and WebSockets.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py3_install

%if %{with test}
%check
# run tests, disable websocket tests and ignore warnings as those tests need updated.
# for more info: https://github.com/encode/uvicorn/issues/1908
%{__python} -m pytest --import-mode append -v tests/ -k 'not websocket' --pythonwarnings 'ignore:websockets:DeprecationWarning'

%endif

%files
%{_bindir}/%{module}
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
%license LICENSE.md
