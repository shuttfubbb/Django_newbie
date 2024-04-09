class DatabaseRouter:
    route_app_mongoDB = {'category', 'product', 'mobile'}
    route_app_mySQL = {'cart'}
                       
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_mongoDB:
            return 'mongoDB'
        
        if model._meta.app_label in self.route_app_mySQL:
            return 'mySQL'
        
        return 
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_mongoDB:
            return 'mongoDB'
        
        if model._meta.app_label in self.route_app_mySQL:
            return 'mySQL'
        
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set = {"default", "mySQL", "mongoDB"}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_mongoDB:
            return db == 'mongoDB'
        
        if app_label in self.route_app_mySQL:
            return db == 'mySQL'
        
        return None