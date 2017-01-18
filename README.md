
System prerequisites
--------------------

1. Install pip:

  ```
  wget https://bootstrap.pypa.io/get-pip.py
  sudo python get-pip.py
  ```

2. Install virtualenv

  ```
  sudo pip install virtualenv
  ```

Project installation
--------------------

1. Clone repository:

  ```
  git clone https://github.com/awp2016/BetX.git
  ```

2. Create virtual environment:

  ```
  cd BetX
  virtualenv sandbox
  ```

3. Activate environment:

  ```
  source sandbox/bin/activate
  ```

4. Apply migrations:

  ```
  ./manage.py migrate
  ```

5. Run development server:

  ```
  ./manage.py runserver
  ```
