import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import cdk8s as _cdk8s_d3d9af27
import constructs as _constructs_77d1e7e8


class CronTab(
    _cdk8s_d3d9af27.ApiObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="comexamplestable.CronTab",
):
    '''
    :schema: CronTab
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
        spec: typing.Optional[typing.Union["CronTabSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Defines a "CronTab" API object.

        :param scope: the scope in which to define this object.
        :param id: a scope-local name for the object.
        :param metadata: 
        :param spec: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35e3deeaa934c86c08854096e921a6efa46a7163083e2c01089896d36c02f9a8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CronTabProps(metadata=metadata, spec=spec)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="manifest")
    @builtins.classmethod
    def manifest(
        cls,
        *,
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
        spec: typing.Optional[typing.Union["CronTabSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> typing.Any:
        '''Renders a Kubernetes manifest for "CronTab".

        This can be used to inline resource manifests inside other objects (e.g. as templates).

        :param metadata: 
        :param spec: 
        '''
        props = CronTabProps(metadata=metadata, spec=spec)

        return typing.cast(typing.Any, jsii.sinvoke(cls, "manifest", [props]))

    @jsii.member(jsii_name="toJson")
    def to_json(self) -> typing.Any:
        '''Renders the object to Kubernetes JSON.'''
        return typing.cast(typing.Any, jsii.invoke(self, "toJson", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GVK")
    def GVK(cls) -> _cdk8s_d3d9af27.GroupVersionKind:
        '''Returns the apiVersion and kind for "CronTab".'''
        return typing.cast(_cdk8s_d3d9af27.GroupVersionKind, jsii.sget(cls, "GVK"))


@jsii.data_type(
    jsii_type="comexamplestable.CronTabProps",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata", "spec": "spec"},
)
class CronTabProps:
    def __init__(
        self,
        *,
        metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
        spec: typing.Optional[typing.Union["CronTabSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metadata: 
        :param spec: 

        :schema: CronTab
        '''
        if isinstance(metadata, dict):
            metadata = _cdk8s_d3d9af27.ApiObjectMetadata(**metadata)
        if isinstance(spec, dict):
            spec = CronTabSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55d9e2e8559872207304a036e062247049f221fcd481acb9b5b042edd0014998)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if metadata is not None:
            self._values["metadata"] = metadata
        if spec is not None:
            self._values["spec"] = spec

    @builtins.property
    def metadata(self) -> typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata]:
        '''
        :schema: CronTab#metadata
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[_cdk8s_d3d9af27.ApiObjectMetadata], result)

    @builtins.property
    def spec(self) -> typing.Optional["CronTabSpec"]:
        '''
        :schema: CronTab#spec
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["CronTabSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CronTabProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="comexamplestable.CronTabSpec",
    jsii_struct_bases=[],
    name_mapping={"cron_spec": "cronSpec", "image": "image", "replicas": "replicas"},
)
class CronTabSpec:
    def __init__(
        self,
        *,
        cron_spec: typing.Optional[builtins.str] = None,
        image: typing.Optional[builtins.str] = None,
        replicas: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cron_spec: 
        :param image: 
        :param replicas: 

        :schema: CronTabSpec
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6102c3cab5ceb6e3f09f7447387dd1faa38dbdb1d8496fb6613acae82f20c0fb)
            check_type(argname="argument cron_spec", value=cron_spec, expected_type=type_hints["cron_spec"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument replicas", value=replicas, expected_type=type_hints["replicas"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cron_spec is not None:
            self._values["cron_spec"] = cron_spec
        if image is not None:
            self._values["image"] = image
        if replicas is not None:
            self._values["replicas"] = replicas

    @builtins.property
    def cron_spec(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CronTabSpec#cronSpec
        '''
        result = self._values.get("cron_spec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image(self) -> typing.Optional[builtins.str]:
        '''
        :schema: CronTabSpec#image
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replicas(self) -> typing.Optional[jsii.Number]:
        '''
        :schema: CronTabSpec#replicas
        '''
        result = self._values.get("replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CronTabSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CronTab",
    "CronTabProps",
    "CronTabSpec",
]

publication.publish()

def _typecheckingstub__35e3deeaa934c86c08854096e921a6efa46a7163083e2c01089896d36c02f9a8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    spec: typing.Optional[typing.Union[CronTabSpec, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d9e2e8559872207304a036e062247049f221fcd481acb9b5b042edd0014998(
    *,
    metadata: typing.Optional[typing.Union[_cdk8s_d3d9af27.ApiObjectMetadata, typing.Dict[builtins.str, typing.Any]]] = None,
    spec: typing.Optional[typing.Union[CronTabSpec, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6102c3cab5ceb6e3f09f7447387dd1faa38dbdb1d8496fb6613acae82f20c0fb(
    *,
    cron_spec: typing.Optional[builtins.str] = None,
    image: typing.Optional[builtins.str] = None,
    replicas: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
