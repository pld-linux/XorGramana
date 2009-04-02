Summary:	Logic word puzzle game
Summary(pl.UTF-8):	Słowana gra logiczna
Name:		XorGramana
Version:	0.0.8
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://www.jwm-art.net/XorGramana/%{name}-%{version}.tar.bz2
# Source0-md5:	24cced5953ea9331f580bc5e6ebf4e87
Patch0:		%{name}-ldflags.patch
URL:		http://www.jwm-art.net/XorGramana/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL_image-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XorGramana is a maze based logical puzzle game where you must escape
each maze by arranging letters to form pre-defined words. There is no
time limit but your total number of movements are restricted. Some
objects move, some explode, and some will kill the player.

%description -l pl.UTF-8
XorGramana to logiczna gra słowna, której głównym elementem są
labirynty. Zadaniem gracza jest wydostanie się z labiryntu
układając litery w odpowiednie słowa. Nie ma limitu czasowego za to
liczba ruchów jest ograniczona. Niektóre obiekty da się przesuwać,
inne wybuchają, a jeszcze inne mogą zabić gracza.

%prep
%setup -q
%patch0 -p1

%build
SDL_CFLAGS=$(sdl-config --cflags)
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} $SDL_CFLAGS -DDATADIR=\'%{_datadir}/%{name}\'" \
	LDFLAGS="%{rpmldflags}" \
	LIBS="-lGLU -lSDL_image"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install xorgramana $RPM_BUILD_ROOT%{_bindir}
cp -r {GFX,data/*} $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/xorgramana
%{_datadir}/%{name}
