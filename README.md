Illustrates "mixins"

Mixins are part of multiple inheritance. They allow for subclasses to inherit specialized functionality.

ProtectedHttpResponse inherits from both HttpResponse and AuthenticatorMixin.  It "really" inherits from HttpResponse, but gains a specific ability from AuthenticatorMixin.  AuthenticatorMixin could be reused in lots of other components.