module.exports = {
  apps: [
    {
      name: "plone",
      script: "source env/bin/activate && runwsgi -v profiles/etc/zope.ini",
    },
  ],
};
